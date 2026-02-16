"""EcucReferenceValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class EcucReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucReferenceValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Referrable,
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize EcucReferenceValue."""
        super().__init__()
        self.value: Optional[Referrable] = None


class EcucReferenceValueBuilder:
    """Builder for EcucReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucReferenceValue = EcucReferenceValue()

    def build(self) -> EcucReferenceValue:
        """Build and return EcucReferenceValue object.

        Returns:
            EcucReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
