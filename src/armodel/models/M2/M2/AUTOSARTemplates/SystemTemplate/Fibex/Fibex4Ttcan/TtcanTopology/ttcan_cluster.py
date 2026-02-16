"""TtcanCluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class TtcanCluster(ARObject):
    """AUTOSAR TtcanCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "basic_cycle_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # basicCycleLength
        "ntu": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ntu
        "operation_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # operationMode
    }

    def __init__(self) -> None:
        """Initialize TtcanCluster."""
        super().__init__()
        self.basic_cycle_length: Optional[Integer] = None
        self.ntu: Optional[TimeValue] = None
        self.operation_mode: Optional[Boolean] = None


class TtcanClusterBuilder:
    """Builder for TtcanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCluster = TtcanCluster()

    def build(self) -> TtcanCluster:
        """Build and return TtcanCluster object.

        Returns:
            TtcanCluster instance
        """
        # TODO: Add validation
        return self._obj
