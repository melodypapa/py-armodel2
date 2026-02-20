"""RptExecutableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)


class RptExecutableEntity(Identifiable):
    """AUTOSAR RptExecutableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rpt_executable_entities: list[RptExecutableEntity]
    rpt_reads: list[RoleBasedMcDataAssignment]
    rpt_writes: list[RoleBasedMcDataAssignment]
    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RptExecutableEntity."""
        super().__init__()
        self.rpt_executable_entities: list[RptExecutableEntity] = []
        self.rpt_reads: list[RoleBasedMcDataAssignment] = []
        self.rpt_writes: list[RoleBasedMcDataAssignment] = []
        self.symbol: Optional[CIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RptExecutableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptExecutableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rpt_executable_entities (list to container "RPT-EXECUTABLE-ENTITIES")
        if self.rpt_executable_entities:
            wrapper = ET.Element("RPT-EXECUTABLE-ENTITIES")
            for item in self.rpt_executable_entities:
                serialized = ARObject._serialize_item(item, "RptExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_reads (list to container "RPT-READS")
        if self.rpt_reads:
            wrapper = ET.Element("RPT-READS")
            for item in self.rpt_reads:
                serialized = ARObject._serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_writes (list to container "RPT-WRITES")
        if self.rpt_writes:
            wrapper = ET.Element("RPT-WRITES")
            for item in self.rpt_writes:
                serialized = ARObject._serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = ARObject._serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntity":
        """Deserialize XML element to RptExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptExecutableEntity, cls).deserialize(element)

        # Parse rpt_executable_entities (list from container "RPT-EXECUTABLE-ENTITIES")
        obj.rpt_executable_entities = []
        container = ARObject._find_child_element(element, "RPT-EXECUTABLE-ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_executable_entities.append(child_value)

        # Parse rpt_reads (list from container "RPT-READS")
        obj.rpt_reads = []
        container = ARObject._find_child_element(element, "RPT-READS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_reads.append(child_value)

        # Parse rpt_writes (list from container "RPT-WRITES")
        obj.rpt_writes = []
        container = ARObject._find_child_element(element, "RPT-WRITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_writes.append(child_value)

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class RptExecutableEntityBuilder:
    """Builder for RptExecutableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutableEntity = RptExecutableEntity()

    def build(self) -> RptExecutableEntity:
        """Build and return RptExecutableEntity object.

        Returns:
            RptExecutableEntity instance
        """
        # TODO: Add validation
        return self._obj
