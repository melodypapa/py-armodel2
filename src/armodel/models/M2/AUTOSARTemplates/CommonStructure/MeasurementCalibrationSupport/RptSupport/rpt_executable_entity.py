"""RptExecutableEntity AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)


class RptExecutableEntity(Identifiable):
    """AUTOSAR RptExecutableEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rpt_executable_entities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptExecutableEntity,
        ),  # rptExecutableEntities
        "rpt_reads": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedMcDataAssignment,
        ),  # rptReads
        "rpt_writes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedMcDataAssignment,
        ),  # rptWrites
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
    }

    def __init__(self) -> None:
        """Initialize RptExecutableEntity."""
        super().__init__()
        self.rpt_executable_entities: list[RptExecutableEntity] = []
        self.rpt_reads: list[RoleBasedMcDataAssignment] = []
        self.rpt_writes: list[RoleBasedMcDataAssignment] = []
        self.symbol: Optional[CIdentifier] = None


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
