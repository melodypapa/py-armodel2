"""CanXlFrameTriggeringProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-XL-FRAME-TRIGGERING-PROPS"


    acceptance_field: Optional[PositiveInteger]
    priority_id: Optional[PositiveInteger]
    sdu_type: Optional[PositiveInteger]
    vcid: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACCEPTANCE-FIELD": lambda obj, elem: setattr(obj, "acceptance_field", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PRIORITY-ID": lambda obj, elem: setattr(obj, "priority_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SDU-TYPE": lambda obj, elem: setattr(obj, "sdu_type", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VCID": lambda obj, elem: setattr(obj, "vcid", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CanXlFrameTriggeringProps."""
        super().__init__()
        self.acceptance_field: Optional[PositiveInteger] = None
        self.priority_id: Optional[PositiveInteger] = None
        self.sdu_type: Optional[PositiveInteger] = None
        self.vcid: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CanXlFrameTriggeringProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanXlFrameTriggeringProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acceptance_field
        if self.acceptance_field is not None:
            serialized = SerializationHelper.serialize_item(self.acceptance_field, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCEPTANCE-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority_id
        if self.priority_id is not None:
            serialized = SerializationHelper.serialize_item(self.priority_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_type
        if self.sdu_type is not None:
            serialized = SerializationHelper.serialize_item(self.sdu_type, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDU-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vcid
        if self.vcid is not None:
            serialized = SerializationHelper.serialize_item(self.vcid, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VCID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanXlFrameTriggeringProps":
        """Deserialize XML element to CanXlFrameTriggeringProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanXlFrameTriggeringProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanXlFrameTriggeringProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCEPTANCE-FIELD":
                setattr(obj, "acceptance_field", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PRIORITY-ID":
                setattr(obj, "priority_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SDU-TYPE":
                setattr(obj, "sdu_type", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VCID":
                setattr(obj, "vcid", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CanXlFrameTriggeringPropsBuilder(BuilderBase):
    """Builder for CanXlFrameTriggeringProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()


    def with_acceptance_field(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringPropsBuilder":
        """Set acceptance_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'acceptance_field' is required and cannot be None")
        self._obj.acceptance_field = value
        return self

    def with_priority_id(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringPropsBuilder":
        """Set priority_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'priority_id' is required and cannot be None")
        self._obj.priority_id = value
        return self

    def with_sdu_type(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringPropsBuilder":
        """Set sdu_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sdu_type' is required and cannot be None")
        self._obj.sdu_type = value
        return self

    def with_vcid(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringPropsBuilder":
        """Set vcid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vcid' is required and cannot be None")
        self._obj.vcid = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "acceptanceField",
        "priorityId",
        "sduType",
        "vcid",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return the CanXlFrameTriggeringProps instance with validation."""
        self._validate_instance()
        return self._obj