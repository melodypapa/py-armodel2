"""EcucAbstractReferenceValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)


class EcucAbstractReferenceValue(EcucIndexableValue):
    """AUTOSAR EcucAbstractReferenceValue."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Annotation,
        ),  # annotations
        "definition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucAbstractReference),
        ),  # definition
        "is_auto_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isAutoValue
    }

    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition: Optional[Any] = None
        self.is_auto_value: Optional[Boolean] = None


class EcucAbstractReferenceValueBuilder:
    """Builder for EcucAbstractReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceValue = EcucAbstractReferenceValue()

    def build(self) -> EcucAbstractReferenceValue:
        """Build and return EcucAbstractReferenceValue object.

        Returns:
            EcucAbstractReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
