"""RptExecutableEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)


class RptExecutableEntity(Identifiable):
    """AUTOSAR RptExecutableEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rpt_executable_entities", None, False, True, RptExecutableEntity),  # rptExecutableEntities
        ("rpt_reads", None, False, True, RoleBasedMcDataAssignment),  # rptReads
        ("rpt_writes", None, False, True, RoleBasedMcDataAssignment),  # rptWrites
        ("symbol", None, True, False, None),  # symbol
    ]

    def __init__(self) -> None:
        """Initialize RptExecutableEntity."""
        super().__init__()
        self.rpt_executable_entities: list[RptExecutableEntity] = []
        self.rpt_reads: list[RoleBasedMcDataAssignment] = []
        self.rpt_writes: list[RoleBasedMcDataAssignment] = []
        self.symbol: Optional[CIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptExecutableEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntity":
        """Create RptExecutableEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptExecutableEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptExecutableEntity since parent returns ARObject
        return cast("RptExecutableEntity", obj)


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
