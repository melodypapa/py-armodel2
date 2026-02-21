"""LinErrorResponse AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class LinErrorResponse(ARObject):
    """AUTOSAR LinErrorResponse."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    response_error_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize LinErrorResponse."""
        super().__init__()
        self.response_error_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinErrorResponse to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinErrorResponse, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize response_error_ref
        if self.response_error_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_error_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ERROR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinErrorResponse":
        """Deserialize XML element to LinErrorResponse object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinErrorResponse object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinErrorResponse, cls).deserialize(element)

        # Parse response_error_ref
        child = SerializationHelper.find_child_element(element, "RESPONSE-ERROR-REF")
        if child is not None:
            response_error_ref_value = ARRef.deserialize(child)
            obj.response_error_ref = response_error_ref_value

        return obj



class LinErrorResponseBuilder:
    """Builder for LinErrorResponse."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinErrorResponse = LinErrorResponse()

    def build(self) -> LinErrorResponse:
        """Build and return LinErrorResponse object.

        Returns:
            LinErrorResponse instance
        """
        # TODO: Add validation
        return self._obj
