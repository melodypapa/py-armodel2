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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntity":
        """Deserialize XML element to RptExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rpt_executable_entities (list)
        obj.rpt_executable_entities = []
        for child in ARObject._find_all_child_elements(element, "RPT-EXECUTABLE-ENTITIES"):
            rpt_executable_entities_value = ARObject._deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entities.append(rpt_executable_entities_value)

        # Parse rpt_reads (list)
        obj.rpt_reads = []
        for child in ARObject._find_all_child_elements(element, "RPT-READS"):
            rpt_reads_value = ARObject._deserialize_by_tag(child, "RoleBasedMcDataAssignment")
            obj.rpt_reads.append(rpt_reads_value)

        # Parse rpt_writes (list)
        obj.rpt_writes = []
        for child in ARObject._find_all_child_elements(element, "RPT-WRITES"):
            rpt_writes_value = ARObject._deserialize_by_tag(child, "RoleBasedMcDataAssignment")
            obj.rpt_writes.append(rpt_writes_value)

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
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
