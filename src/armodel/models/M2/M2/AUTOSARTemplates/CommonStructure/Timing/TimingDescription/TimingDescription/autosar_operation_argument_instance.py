"""AutosarOperationArgumentInstance AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarOperationArgumentInstance(Identifiable):
    """AUTOSAR AutosarOperationArgumentInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # operation
    }

    def __init__(self) -> None:
        """Initialize AutosarOperationArgumentInstance."""
        super().__init__()
        self.operation: Optional[DataPrototype] = None


class AutosarOperationArgumentInstanceBuilder:
    """Builder for AutosarOperationArgumentInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarOperationArgumentInstance = AutosarOperationArgumentInstance()

    def build(self) -> AutosarOperationArgumentInstance:
        """Build and return AutosarOperationArgumentInstance object.

        Returns:
            AutosarOperationArgumentInstance instance
        """
        # TODO: Add validation
        return self._obj
