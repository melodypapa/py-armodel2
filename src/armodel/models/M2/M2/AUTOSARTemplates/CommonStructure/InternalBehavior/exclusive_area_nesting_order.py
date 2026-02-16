"""ExclusiveAreaNestingOrder AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class ExclusiveAreaNestingOrder(Referrable):
    """AUTOSAR ExclusiveAreaNestingOrder."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "exclusive_areas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveArea,
        ),  # exclusiveAreas
    }

    def __init__(self) -> None:
        """Initialize ExclusiveAreaNestingOrder."""
        super().__init__()
        self.exclusive_areas: list[ExclusiveArea] = []


class ExclusiveAreaNestingOrderBuilder:
    """Builder for ExclusiveAreaNestingOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveAreaNestingOrder = ExclusiveAreaNestingOrder()

    def build(self) -> ExclusiveAreaNestingOrder:
        """Build and return ExclusiveAreaNestingOrder object.

        Returns:
            ExclusiveAreaNestingOrder instance
        """
        # TODO: Add validation
        return self._obj
