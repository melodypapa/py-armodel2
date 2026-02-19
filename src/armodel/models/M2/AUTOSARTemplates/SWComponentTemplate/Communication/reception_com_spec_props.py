"""ReceptionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ReceptionComSpecProps(ARObject):
    """AUTOSAR ReceptionComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_update: Optional[TimeValue]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ReceptionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize ReceptionComSpecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize data_update
        if self.data_update is not None:
            serialized = ARObject._serialize_item(self.data_update, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = ARObject._serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceptionComSpecProps":
        """Deserialize XML element to ReceptionComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceptionComSpecProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_update
        child = ARObject._find_child_element(element, "DATA-UPDATE")
        if child is not None:
            data_update_value = child.text
            obj.data_update = data_update_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class ReceptionComSpecPropsBuilder:
    """Builder for ReceptionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceptionComSpecProps = ReceptionComSpecProps()

    def build(self) -> ReceptionComSpecProps:
        """Build and return ReceptionComSpecProps object.

        Returns:
            ReceptionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
