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

    assigned: Optional[LinSlave]
    assigned_lin: Optional[LinSlaveConfigIdent]
    def __init__(self) -> None:
        """Initialize LinConfigurationEntry."""
        super().__init__()
        self.assigned: Optional[LinSlave] = None
        self.assigned_lin: Optional[LinSlaveConfigIdent] = None
    def serialize(self) -> ET.Element:
        """Serialize LinConfigurationEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinConfigurationEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned
        if self.assigned is not None:
            serialized = ARObject._serialize_item(self.assigned, "LinSlave")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize assigned_lin
        if self.assigned_lin is not None:
            serialized = ARObject._serialize_item(self.assigned_lin, "LinSlaveConfigIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-LIN")
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

        # Parse assigned
        child = ARObject._find_child_element(element, "ASSIGNED")
        if child is not None:
            assigned_value = ARObject._deserialize_by_tag(child, "LinSlave")
            obj.assigned = assigned_value

        # Parse assigned_lin
        child = ARObject._find_child_element(element, "ASSIGNED-LIN")
        if child is not None:
            assigned_lin_value = ARObject._deserialize_by_tag(child, "LinSlaveConfigIdent")
            obj.assigned_lin = assigned_lin_value

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
