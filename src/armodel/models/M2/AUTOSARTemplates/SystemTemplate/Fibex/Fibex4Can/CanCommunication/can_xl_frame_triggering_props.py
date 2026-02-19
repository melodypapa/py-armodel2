"""CanXlFrameTriggeringProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acceptance_field: Optional[PositiveInteger]
    priority_id: Optional[PositiveInteger]
    sdu_type: Optional[PositiveInteger]
    vcid: Optional[PositiveInteger]
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
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize acceptance_field
        if self.acceptance_field is not None:
            serialized = ARObject._serialize_item(self.acceptance_field, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.priority_id, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.sdu_type, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.vcid, "PositiveInteger")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse acceptance_field
        child = ARObject._find_child_element(element, "ACCEPTANCE-FIELD")
        if child is not None:
            acceptance_field_value = child.text
            obj.acceptance_field = acceptance_field_value

        # Parse priority_id
        child = ARObject._find_child_element(element, "PRIORITY-ID")
        if child is not None:
            priority_id_value = child.text
            obj.priority_id = priority_id_value

        # Parse sdu_type
        child = ARObject._find_child_element(element, "SDU-TYPE")
        if child is not None:
            sdu_type_value = child.text
            obj.sdu_type = sdu_type_value

        # Parse vcid
        child = ARObject._find_child_element(element, "VCID")
        if child is not None:
            vcid_value = child.text
            obj.vcid = vcid_value

        return obj



class CanXlFrameTriggeringPropsBuilder:
    """Builder for CanXlFrameTriggeringProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()

    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return CanXlFrameTriggeringProps object.

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # TODO: Add validation
        return self._obj
