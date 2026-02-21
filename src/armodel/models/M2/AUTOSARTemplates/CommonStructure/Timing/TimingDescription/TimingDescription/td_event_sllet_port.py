"""TDEventSLLETPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class TDEventSLLETPort(TDEventSLLET):
    """AUTOSAR TDEventSLLETPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventSLLETPort."""
        super().__init__()
        self.port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventSLLETPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSLLETPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_ref
        if self.port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSLLETPort":
        """Deserialize XML element to TDEventSLLETPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSLLETPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSLLETPort, cls).deserialize(element)

        # Parse port_ref
        child = SerializationHelper.find_child_element(element, "PORT-REF")
        if child is not None:
            port_ref_value = ARRef.deserialize(child)
            obj.port_ref = port_ref_value

        return obj



class TDEventSLLETPortBuilder:
    """Builder for TDEventSLLETPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSLLETPort = TDEventSLLETPort()

    def build(self) -> TDEventSLLETPort:
        """Build and return TDEventSLLETPort object.

        Returns:
            TDEventSLLETPort instance
        """
        # TODO: Add validation
        return self._obj
