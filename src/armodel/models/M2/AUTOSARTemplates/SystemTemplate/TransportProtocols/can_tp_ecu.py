"""CanTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CanTpEcu(ARObject):
    """AUTOSAR CanTpEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cycle_time_main: Optional[TimeValue]
    ecu_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CanTpEcu."""
        super().__init__()
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CanTpEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanTpEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cycle_time_main
        if self.cycle_time_main is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_time_main, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-TIME-MAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpEcu":
        """Deserialize XML element to CanTpEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanTpEcu, cls).deserialize(element)

        # Parse cycle_time_main
        child = SerializationHelper.find_child_element(element, "CYCLE-TIME-MAIN")
        if child is not None:
            cycle_time_main_value = child.text
            obj.cycle_time_main = cycle_time_main_value

        # Parse ecu_instance_ref
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        return obj



class CanTpEcuBuilder:
    """Builder for CanTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpEcu = CanTpEcu()

    def build(self) -> CanTpEcu:
        """Build and return CanTpEcu object.

        Returns:
            CanTpEcu instance
        """
        # TODO: Add validation
        return self._obj
