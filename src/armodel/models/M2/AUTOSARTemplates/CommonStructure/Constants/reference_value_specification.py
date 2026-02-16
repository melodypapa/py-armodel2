"""ReferenceValueSpecification AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class ReferenceValueSpecification(ValueSpecification):
    """AUTOSAR ReferenceValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "reference_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # referenceValue
    }

    def __init__(self) -> None:
        """Initialize ReferenceValueSpecification."""
        super().__init__()
        self.reference_value: Optional[DataPrototype] = None


class ReferenceValueSpecificationBuilder:
    """Builder for ReferenceValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceValueSpecification = ReferenceValueSpecification()

    def build(self) -> ReferenceValueSpecification:
        """Build and return ReferenceValueSpecification object.

        Returns:
            ReferenceValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
