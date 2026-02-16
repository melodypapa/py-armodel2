"""NotAvailableValueSpecification AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NotAvailableValueSpecification(ValueSpecification):
    """AUTOSAR NotAvailableValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_pattern": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultPattern
    }

    def __init__(self) -> None:
        """Initialize NotAvailableValueSpecification."""
        super().__init__()
        self.default_pattern: Optional[PositiveInteger] = None


class NotAvailableValueSpecificationBuilder:
    """Builder for NotAvailableValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NotAvailableValueSpecification = NotAvailableValueSpecification()

    def build(self) -> NotAvailableValueSpecification:
        """Build and return NotAvailableValueSpecification object.

        Returns:
            NotAvailableValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
