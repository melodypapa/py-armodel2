"""CanTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    ecu_instance: Optional[EcuInstance]
    def __init__(self) -> None:
        """Initialize CanTpEcu."""
        super().__init__()
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None

    def serialize(self) -> ET.Element:
        """Serialize CanTpEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize cycle_time_main
        if self.cycle_time_main is not None:
            serialized = ARObject._serialize_item(self.cycle_time_main, "TimeValue")
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

        # Serialize ecu_instance
        if self.ecu_instance is not None:
            serialized = ARObject._serialize_item(self.ecu_instance, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cycle_time_main
        child = ARObject._find_child_element(element, "CYCLE-TIME-MAIN")
        if child is not None:
            cycle_time_main_value = child.text
            obj.cycle_time_main = cycle_time_main_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

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
