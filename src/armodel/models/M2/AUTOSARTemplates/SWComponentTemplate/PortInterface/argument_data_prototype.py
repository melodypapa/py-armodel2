"""ArgumentDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1998)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 29)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)


class ArgumentDataPrototype(AutosarDataPrototype):
    """AUTOSAR ArgumentDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "direction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArgumentDirectionEnum,
        ),  # direction
        "server_argument_impl": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ServerArgumentImplPolicyEnum,
        ),  # serverArgumentImpl
    }

    def __init__(self) -> None:
        """Initialize ArgumentDataPrototype."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.server_argument_impl: Optional[ServerArgumentImplPolicyEnum] = None


class ArgumentDataPrototypeBuilder:
    """Builder for ArgumentDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArgumentDataPrototype = ArgumentDataPrototype()

    def build(self) -> ArgumentDataPrototype:
        """Build and return ArgumentDataPrototype object.

        Returns:
            ArgumentDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
