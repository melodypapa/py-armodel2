"""ModePortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import GeneralAnnotationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModePortAnnotation(GeneralAnnotation):
    """AUTOSAR ModePortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-PORT-ANNOTATION"


    mode_group_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MODE-GROUP-REF": lambda obj, elem: setattr(obj, "mode_group_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModePortAnnotation."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModePortAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModePortAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModePortAnnotation":
        """Deserialize XML element to ModePortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModePortAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModePortAnnotation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-GROUP-REF":
                setattr(obj, "mode_group_ref", ARRef.deserialize(child))

        return obj



class ModePortAnnotationBuilder(GeneralAnnotationBuilder):
    """Builder for ModePortAnnotation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModePortAnnotation = ModePortAnnotation()


    def with_mode_group(self, value: Optional[ModeDeclarationGroup]) -> "ModePortAnnotationBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mode_group' is required and cannot be None")
        self._obj.mode_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "modeGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModePortAnnotation:
        """Build and return the ModePortAnnotation instance with validation."""
        self._validate_instance()
        return self._obj