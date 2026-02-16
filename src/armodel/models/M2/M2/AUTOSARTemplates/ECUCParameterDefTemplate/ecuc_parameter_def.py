"""EcucParameterDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)


class EcucParameterDef(EcucCommonAttributes):
    """AUTOSAR EcucParameterDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "derivation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucDerivationSpecification,
        ),  # derivation
        "symbolic_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbolicName
        "with_auto": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # withAuto
    }

    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None


class EcucParameterDefBuilder:
    """Builder for EcucParameterDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDef = EcucParameterDef()

    def build(self) -> EcucParameterDef:
        """Build and return EcucParameterDef object.

        Returns:
            EcucParameterDef instance
        """
        # TODO: Add validation
        return self._obj
