"""ApplicationCompositeElementDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationCompositeElementDataPrototype(DataPrototype):
    """AUTOSAR ApplicationCompositeElementDataPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationDataType,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementDataPrototype."""
        super().__init__()
        self.type: Optional[ApplicationDataType] = None


class ApplicationCompositeElementDataPrototypeBuilder:
    """Builder for ApplicationCompositeElementDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementDataPrototype = ApplicationCompositeElementDataPrototype()

    def build(self) -> ApplicationCompositeElementDataPrototype:
        """Build and return ApplicationCompositeElementDataPrototype object.

        Returns:
            ApplicationCompositeElementDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
