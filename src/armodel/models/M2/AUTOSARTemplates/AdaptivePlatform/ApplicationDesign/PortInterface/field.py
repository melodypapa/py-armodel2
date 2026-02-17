"""Field AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_ApplicationDesign_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "has_getter": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # hasGetter
        "has_notifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # hasNotifier
        "has_setter": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # hasSetter
    }

    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None


class FieldBuilder:
    """Builder for Field."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Field = Field()

    def build(self) -> Field:
        """Build and return Field object.

        Returns:
            Field instance
        """
        # TODO: Add validation
        return self._obj
