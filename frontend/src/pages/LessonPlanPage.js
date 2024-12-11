import React, { useState, useRef } from "react";
import JoditEditor from "jodit-react";
import '../styling/EditCourse.css';

const LessonPlanPage = () => {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    title: "Title",
    duration: "2021-04-05 to 2021-04-09",
    standards: [
      "Standard 1",
      "Standard 2",
      "Standard 3",
    ],
    learningObjective:
      "Objectives",
    essentialQuestion: "Essential question",
    lessonDescription:
      "Unit description",
  });

  const handleInputChange = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  return (
    <div className="lesson-plan-container">
      <h1>Unit Overview</h1>
      <button
        onClick={() => setIsEditing(!isEditing)}
        className="toggle-button"
      >
        {isEditing ? "View Mode" : "Edit Mode"}
      </button>

      <div className="field-container">
        <label>Unit:</label>
        {isEditing ? (
          <input
            type="text"
            value={formData.title}
            onChange={(e) => handleInputChange("title", e.target.value)}
          />
        ) : (
          <p>{formData.title}</p>
        )}
      </div>

      <div className="field-container">
        <label>Duration:</label>
        {isEditing ? (
          <input
            type="text"
            value={formData.duration}
            onChange={(e) => handleInputChange("duration", e.target.value)}
          />
        ) : (
          <p>{formData.duration}</p>
        )}
      </div>

      <div className="field-container">
        <label>Standards:</label>
        {isEditing ? (
          <textarea
            value={formData.standards.join("\n")}
            onChange={(e) =>
              handleInputChange("standards", e.target.value.split("\n"))
            }
          />
        ) : (
          <ul>
            {formData.standards.map((standard, index) => (
              <li key={index}>{standard}</li>
            ))}
          </ul>
        )}
      </div>

      <div className="field-container">
        <label>Integrated Learning Objective:</label>
        {isEditing ? (
          <JoditEditor
            value={formData.learningObjective}
            onBlur={(newContent) =>
              handleInputChange("learningObjective", newContent)
            }
          />
        ) : (
          <p dangerouslySetInnerHTML={{ __html: formData.learningObjective }} />
        )}
      </div>

      <div className="field-container">
        <label>Inclusive Essential Question:</label>
        {isEditing ? (
          <JoditEditor
            value={formData.essentialQuestion}
            onBlur={(newContent) =>
              handleInputChange("essentialQuestion", newContent)
            }
          />
        ) : (
          <p dangerouslySetInnerHTML={{ __html: formData.essentialQuestion }} />
        )}
      </div>

      <div className="field-container">
        <label>Lesson Description:</label>
        {isEditing ? (
          <JoditEditor
            value={formData.lessonDescription}
            onBlur={(newContent) =>
              handleInputChange("lessonDescription", newContent)
            }
          />
        ) : (
          <p dangerouslySetInnerHTML={{ __html: formData.lessonDescription }} />
        )}
      </div>
    </div>
  );
};

export default LessonPlanPage;
