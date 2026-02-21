"""LinConfigurationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave import (
    LinSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)
from abc import ABC, abstractmethod


class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """AUTOSAR LinConfigurationEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    assigned_ref: Optional[ARRef]
    assigned_lin_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize LinConfigurationEntry."""
        super().__init__()
        self.assigned_ref: Optional[ARRef] = None
        self.assigned_lin_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinConfigurationEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinConfigurationEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_ref
        if self.assigned_ref is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_ref, "LinSlave")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize assigned_lin_ref
        if self.assigned_lin_ref is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_lin_ref, "LinSlaveConfigIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-LIN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinConfigurationEntry":
        """Deserialize XML element to LinConfigurationEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinConfigurationEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinConfigurationEntry, cls).deserialize(element)

        # Parse assigned_ref
        child = SerializationHelper.find_child_element(element, "ASSIGNED-REF")
        if child is not None:
            assigned_ref_value = ARRef.deserialize(child)
            obj.assigned_ref = assigned_ref_value

        # Parse assigned_lin_ref
        child = SerializationHelper.find_child_element(element, "ASSIGNED-LIN-REF")
        if child is not None:
            assigned_lin_ref_value = ARRef.deserialize(child)
            obj.assigned_lin_ref = assigned_lin_ref_value

        return obj



class LinConfigurationEntryBuilder:
    """Builder for LinConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinConfigurationEntry = LinConfigurationEntry()

    def build(self) -> LinConfigurationEntry:
        """Build and return LinConfigurationEntry object.

        Returns:
            LinConfigurationEntry instance
        """
        # TODO: Add validation
        return self._obj
