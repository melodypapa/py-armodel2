"""EcuPartition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcuPartition(Identifiable):
    """AUTOSAR EcuPartition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "exec_in_user": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # execInUser
    }

    def __init__(self) -> None:
        """Initialize EcuPartition."""
        super().__init__()
        self.exec_in_user: Optional[Boolean] = None


class EcuPartitionBuilder:
    """Builder for EcuPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuPartition = EcuPartition()

    def build(self) -> EcuPartition:
        """Build and return EcuPartition object.

        Returns:
            EcuPartition instance
        """
        # TODO: Add validation
        return self._obj
