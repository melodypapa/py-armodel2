"""DiagnosticComControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 108)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    com_control_ref: Optional[ARRef]
    custom_sub: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control_ref: Optional[ARRef] = None
        self.custom_sub: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize com_control_ref
        if self.com_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.com_control_ref, "DiagnosticComControl")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize custom_sub
        if self.custom_sub is not None:
            serialized = SerializationHelper.serialize_item(self.custom_sub, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControl":
        """Deserialize XML element to DiagnosticComControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControl, cls).deserialize(element)

        # Parse com_control_ref
        child = SerializationHelper.find_child_element(element, "COM-CONTROL-REF")
        if child is not None:
            com_control_ref_value = ARRef.deserialize(child)
            obj.com_control_ref = com_control_ref_value

        # Parse custom_sub
        child = SerializationHelper.find_child_element(element, "CUSTOM-SUB")
        if child is not None:
            custom_sub_value = child.text
            obj.custom_sub = custom_sub_value

        return obj



class DiagnosticComControlBuilder:
    """Builder for DiagnosticComControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControl = DiagnosticComControl()

    def build(self) -> DiagnosticComControl:
        """Build and return DiagnosticComControl object.

        Returns:
            DiagnosticComControl instance
        """
        # TODO: Add validation
        return self._obj
